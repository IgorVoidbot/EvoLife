"""O loop deve simular o mesmo segundo em diferentes cadências de quadros."""

import pygame
import pytest

import main as application
from evolife.config import FIXED_DT, MAX_FPS
from evolife.creature import Creature
from evolife.renderer import Renderer
from evolife.world import World


@pytest.mark.parametrize(
    "frame_times",
    [[10] * 100, [100] * 10, [1000]],
    ids=["100-fps", "10-fps", "1-fps"],
)
def test_fixed_time_updates_are_independent_of_rendering(monkeypatch, frame_times):
    world = World()
    world.foods.clear()
    world.creatures = [Creature(100.0, 100.0, 0.0, 40.0, wander_remaining=3.0)]
    steps = []
    original_update = world.update

    def update(dt):
        steps.append(dt)
        original_update(dt)

    world.update = update
    monkeypatch.setattr(application, "World", lambda: world)
    times = iter([*frame_times, 0])

    class FakeClock:
        def tick(self, fps):
            assert fps == MAX_FPS
            return next(times)

    monkeypatch.setattr(pygame.time, "Clock", FakeClock)
    original_draw = Renderer.draw
    frames = []

    def draw(self, state):
        original_draw(self, state)
        frames.append(1)
        if len(frames) == len(frame_times):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    monkeypatch.setattr(Renderer, "draw", draw)
    assert application.main() == 0
    assert steps == [FIXED_DT] * 60
    assert len(frames) == len(frame_times)
    assert world.creatures[0].x == pytest.approx(140.0)
    assert world.creatures[0].y == pytest.approx(100.0)
    assert world.creatures[0].energy == pytest.approx(100.0 - 1.33)
    assert len(world.foods) == 1
    assert not pygame.display.get_init()


def test_application_remains_responsive_and_replenishes_after_extinction(monkeypatch):
    world = World()
    world.creatures = [Creature(100, 100, 0, 40, energy=0.001)]
    world.foods.clear()
    monkeypatch.setattr(application, "World", lambda: world)

    class FakeClock:
        def tick(self, fps):
            return 1000

    monkeypatch.setattr(pygame.time, "Clock", FakeClock)
    original_draw = Renderer.draw
    frames = []

    def draw(self, state):
        original_draw(self, state)
        assert state.creatures == []
        frames.append(1)
        if len(frames) == 10:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    monkeypatch.setattr(Renderer, "draw", draw)
    assert application.main() == 0
    assert len(frames) == 10
    assert len(world.foods) == 10
    assert not pygame.display.get_init()
