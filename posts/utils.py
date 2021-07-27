from django.shortcuts import render, get_object_or_404, redirect, reverse


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
        return render(request, self.template, context={'form': form})


class ObjectUpdateMixin:
    bound_form = None
    obj_class = None
    template = None

    def get(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.bound_form(instance=obj)
        return render(request, self.template, context={'form': bound_form,
                                                       self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.bound_form(request.POST, instance=obj)
        if bound_form.is_valid():
            post = bound_form.save()
            return redirect(post)
        return render(request, self.template, context={'form': bound_form,
                                                       self.obj_class.__name__.lower(): obj})


class ObjectDeleteMixin:
    obj_class = None
    template = None
    list_url = None

    def get(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        return render(request, self.template, context={self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        obj.delete()
        return redirect(reverse(self.list_url))
