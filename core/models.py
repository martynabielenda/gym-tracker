from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="exercises"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workouts"
    )
    name = models.CharField(max_length=150)
    workout_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="workout_exercises"
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
        related_name="workout_exercises"
    )
    exercise_order = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["exercise_order"]

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"


class ExerciseSet(models.Model):
    workout_exercise = models.ForeignKey(
        WorkoutExercise,
        on_delete=models.CASCADE,
        related_name="sets"
    )
    set_number = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["set_number"]

    def __str__(self):
        return f"Set {self.set_number}"
