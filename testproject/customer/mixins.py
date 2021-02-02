from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

# class ObjectsListMixin:
#     model = None
#     template = None
#     def get(self, request):
#         objects = self.model.objects.all()
#         paginator = Paginator(objects, 2)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context = {
#             'title': self.model._meta.verbose_name_plural,
#             'fields': self.model._meta.fields,
#             'page_obj': page_obj,
#             'paginator': paginator
#         }
#         return render(request, self.template, context=context)

# class ObjectCreateMixin:
#     form = None
#     model = None
#     template = None
#
#     def get(self, request):
#         form = self.form()
#         context = {
#             'form': form,
#             'title': self.model._meta.verbose_name
#         }
#         return render(request, self.template, context=context)
#
#     def post(self, request):
#         form = self.form(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect(f'{self.model.__name__.lower()}-list')
#         return render(request, self.template, {'form': form})
#
#
# class ObjectUpdateMixin:
#     model = None
#     template = None
#     form = None
#
#     def get(self, request, pk):
#         obj = self.model.objects.get(pk=pk)
#         form = self.form(instance=obj)
#         context = {
#             'obj': obj,
#             'form': form
#         }
#         return render(request, self.template, context=context)
#
#
#     def post(self,request, pk):
#         obj = self.model.objects.get(pk=pk)
#         form = self.form(request.POST, instance=obj)
#
#         if form.is_valid():
#             form.save()
#             return redirect(f'{self.model.__name__.lower()}-list')
#
#
#         context = {
#             'obj': obj,
#             'form': form
#         }
#         return render(request, self.template, context=context)

#
# class ObjectDeleteMixin:
#     model = None
#     template = None
#
#     def get(self, request, pk):
#         obj = self.model.objects.get(pk=pk)
#         return render(request, self.template, {'object':obj})
#
#     def post(self, request, pk):
#         obj = self.model.objects.get(pk=pk)
#         obj.delete()
#         return redirect(f'{self.model.__name__.lower()}-list')