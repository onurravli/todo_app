from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __json__(self):
        return dict(
            title=self.title,
            desc=self.desc,
            done=self.done,
        )
