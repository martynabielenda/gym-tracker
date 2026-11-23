from django.contrib import admin
from .models import Category, Exercise, Workout, WorkoutExercise, ExerciseSet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "workout_date", "duration")
    list_filter = ("workout_date", "user")
    search_fields = ("name", "user__username")
    inlines = [WorkoutExerciseInline]


class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet
    extra = 1


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ("workout", "exercise", "exercise_order")
    inlines = [ExerciseSetInline]


@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ("workout_exercise", "set_number", "repetitions", "weight")
