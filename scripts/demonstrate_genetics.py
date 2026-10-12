"""Demonstração reproduzível da Sprint 4; legendas ficam somente na mídia."""

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import tempfile

from evolife.config import FIXED_DT
from evolife.genetics import GENE_RANGES, Genes
from evolife.world import World


@dataclass(frozen=True)
class BirthExample:
    seconds: float
    parent_id: int
    child_id: int
    generation: int
    parent_genes: Genes
    child_genes: Genes

    @property
    def changed_genes(self) -> str:
        return ", ".join(
            name for name, _, _ in GENE_RANGES
            if getattr(self.parent_genes, name) != getattr(self.child_genes, name)
        ) or "nenhum"


def format_genes(genes: Genes) -> str:
    return f"({genes.speed:.6f}, {genes.vision:.6f}, {genes.efficiency:.6f})"


def render_frame(world: World, seconds: float, birth: BirthExample | None, path: Path) -> None:
    import pygame

    from evolife.renderer import Renderer

    screen = pygame.Surface((800, 600))
    Renderer(screen).draw(world)
    if birth is not None:
        for creature in world.creatures:
            if creature.id in (birth.parent_id, birth.child_id):
                pygame.draw.circle(screen, (255, 210, 80),
                                   (round(creature.x), round(creature.y)), 11, 2)
    pygame.draw.rect(screen, (18, 22, 28), (0, 0, 800, 35))
    pygame.draw.rect(screen, (18, 22, 28), (0, 450, 800, 150))
    font = pygame.font.Font(None, 22)
    lines = [
        "Sprint 4 | seed 42 | mutacao 12%, sigma 8% | genes: speed, vision, efficiency",
        f"t={seconds:.2f}s | tempo da midia: 4x | regras oficiais preservadas",
    ]
    if birth is None:
        lines += ["Geracao inicial 0; aguardando nascimentos.",
                  "Genes na ordem: speed, vision, efficiency."]
    else:
        lines += [
            f"Nascimento em {birth.seconds:.2f}s: ID {birth.parent_id} -> ID {birth.child_id}"
            f" | geracao {birth.generation}",
            f"Progenitor: {format_genes(birth.parent_genes)}",
            f"Descendente: {format_genes(birth.child_genes)}",
            f"Genes alterados: {birth.changed_genes}",
        ]
    for index, line in enumerate(lines):
        y = 10 if index == 0 else 460 + (index - 1) * 25
        screen.blit(font.render(line, True, (230, 235, 240)), (12, y))
    pygame.image.save(screen, path)


def simulate(frame_directory: Path | None = None) -> tuple[World, list[BirthExample], int]:
    """Execute 60 s com parâmetros padrão, sem editar energia, idade ou comida."""
    world = World(seed=42)
    known = {creature.id: creature for creature in world.creatures}
    births = []
    peak_population = len(world.creatures)
    for step in range(1, 3601):
        world.update(FIXED_DT)
        peak_population = max(peak_population, len(world.creatures))
        for creature in world.creatures:
            if creature.id not in known:
                parent = known[creature.parent_id]
                births.append(BirthExample(step * FIXED_DT, parent.id, creature.id,
                                           creature.generation, parent.genes, creature.genes))
                known[creature.id] = creature
        if frame_directory is not None and step % 16 == 0:
            render_frame(world, step * FIXED_DT, births[-1] if births else None,
                         frame_directory / f"{step // 16:04d}.png")
    return world, births, peak_population


def create_gif(frame_directory: Path, output: Path) -> None:
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-framerate", "15",
        "-start_number", "1", "-i", str(frame_directory / "%04d.png"),
        "-filter_complex",
        "[0:v]split[a][b];[a]palettegen[p];[b][p]paletteuse",
        "-loop", "0", str(output),
    ], check=True)


def print_report(world: World, births: list[BirthExample], peak: int) -> None:
    print("# Demonstração genética — Sprint 4\n")
    print("Cenário controlado: `World(seed=42)` com todos os parâmetros oficiais\n"
          "padrão. Área 800 × 600; dez criaturas na geração 0, energia 100,\n"
          "idade/cooldown zero; velocidades iniciais sorteadas entre 25 e 90,\n"
          "visão 100 e eficiência 1. Comida inicial 75, reposição 1/s até 125.\n"
          "3600 passos de 1/60 s, totalizando 60 s lógicos.\n")
    print("Reprodução: idade ≥10 s, energia ≥110 após metabolismo e cooldown\n"
          "encerrado; transferência 45, filhote com energia 45, espera 10 s.\n"
          "Cada gene: chance 12%, normal centrada em zero, desvio de 8% da\n"
          "amplitude (speed 5,2; vision 10; efficiency 0,032); valores limitados\n"
          "às faixas do PRD. Nenhuma regra foi alterada para produzir nascimentos.\n")
    print(f"Resultado: **{world.births_total} nascimentos**, **{world.deaths_total} mortes**,\n"
          f"população máxima **{peak}**, final **{len(world.creatures)}**; geração\n"
          f"máxima observada **{max(b.generation for b in births)}**.\n")
    print("Genes na ordem `(speed, vision, efficiency)`, arredondados a seis casas.\n"
          "IDs e genes foram capturados no nascimento, inclusive de progenitores\n"
          "que morreram depois. 'Nenhum' indica ausência de mudança no valor;\n"
          "um sorteio de mutação com variação nula ou limitada pode não alterá-lo.\n")
    print("| Tempo (s) | Progenitor | Descendente | Geração | Genes do progenitor | Genes do descendente | Genes alterados |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for birth in births:
        print(f"| {birth.seconds:.6f} | {birth.parent_id} | {birth.child_id} | {birth.generation} "
              f"| {format_genes(birth.parent_genes)} | {format_genes(birth.child_genes)} "
              f"| {birth.changed_genes} |")
    print("\nExemplo de linhagem: **8 → 18 → 25 → 35**, gerações **0 → 1 → 2 → 3**.\n"
          "O ID 18 herdou visão/eficiência e teve variação em speed; o ID 25\n"
          "herdou todos os valores; o ID 35 herdou speed/vision e teve variação\n"
          "em efficiency. A execução não apresentou mudança em vision, embora\n"
          "esse gene use a mesma regra independente, validada pelos testes.\n")
    print("Reprodução do relatório, na raiz com o .venv ativado:\n\n"
          "```bash\npython -m scripts.demonstrate_genetics\n```\n\n"
          "A [mídia da Sprint 4](media/sprint4.gif) contém 225 quadros a 15 FPS,\n"
          "15 s de mídia para 60 s lógicos (4x). Renderização fora da tela,\n"
          "sem janela de desktop; legendas e anéis existem somente na mídia.\n"
          "Para regenerar, com ffmpeg disponível:\n\n"
          "```bash\npython -m scripts.demonstrate_genetics --gif docs/media/sprint4.gif\n```\n")
    print("Limites: demonstração de herança e variação em uma execução; não prova\n"
          "adaptação nem favorecimento causal de genes. Sem coleta de médias,\n"
          "HUD ou exportação CSV; não é um experimento comparativo de seleção.\n"
          "A inspeção manual no desktop e a validação Windows estão pendentes.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gif", type=Path, help="opcional: mídia anotada usando ffmpeg")
    args = parser.parse_args()
    if args.gif is None:
        world, births, peak = simulate()
    else:
        import os

        os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
        os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
        import pygame

        pygame.font.init()
        try:
            with tempfile.TemporaryDirectory(prefix="evolife-sprint4-") as temporary:
                frame_directory = Path(temporary)
                world, births, peak = simulate(frame_directory)
                create_gif(frame_directory, args.gif)
        finally:
            pygame.quit()
    print_report(world, births, peak)


if __name__ == "__main__":
    main()
