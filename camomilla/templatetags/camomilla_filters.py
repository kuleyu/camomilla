from django import template
from django.utils.translation import activate, get_language


register = template.Library()


@register.filter(name='filter_content')
def filter_content(page, args):
    try:
        content = page.contents.get(identifier=args)
    except page.contents.model.DoesNotExist:
        content, _ = page.contents.get_or_create(identifier=args)
    if get_language() not in content.get_available_languages():
        content.translate(get_language())
        content.save()
    return content


@register.filter(name='alternate_urls')
def alternate_urls(page, request):
    alternates = page.alternate_urls(request)
    return alternates.get('alternate_urls', alternates).items()
