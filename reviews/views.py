
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


def index(request):
    """Рендер главной страницы."""
    if Review.objects.filter(device_id=request.COOKIES
                             .get('device_token')).exists():
        template = 'already_reviewed.html'
        return render(request, template)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save()
        response = redirect('thanks')
        response.set_cookie('device_token', review.device_id,
                            max_age=31536000, httponly=True,
                            secure=True, samesite='Lax')
        return response
    template = 'index.html'
    context = {'form': form}
    return render(request, template, context)


class ThanksView(TemplateView):
    """Страница с благодарностью за отзыв."""
    template_name = 'thanks.html'


class ReviewListView(PermissionRequiredMixin, ListView):
    """Лист со всеми отзывами, доступен только авторизованным."""
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    permission_required = 'reviews.view_review'
