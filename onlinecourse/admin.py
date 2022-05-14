from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice


# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'lesson_title', 'grade')
    list_filter = ('lesson', 'grade')
    search_fields = ('question_text', 'lesson')
    inlines = [ChoiceInline]

    def lesson_title(self, obj):
        return obj.lesson.title

    def question_text(self, obj):
        return obj.choice_text[:60]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text')
    list_filter = ('is_correct',)
    search_fields = ('choice_text',)

    def text(self, obj):
        return obj.choice_text[:50]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)