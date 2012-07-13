from django import template
import datetime
from django.template.defaultfilters import stringfilter
from mysite.liga.models import TableResults

register = template.Library()

#@register.tag(name='current_time')
#def do_current_time(parser, token):
#    try:
        # split_contents() knows not to split quoted strings.
#        tag_name, format_string = token.split_contents()
#        print tag_name
#    except ValueError:
#        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
#    if not (format_string[0] == format_string[-1] and format_string[0] in ('"',"'")):
#        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
#    return CurrentTimeNode(format_string[1:-1])

#class CurrentTimeNode(template.Node):
#    def __init__(self, format_string):
#        self.format_string = format_string
#    def render(self, context):
@register.simple_tag
def  team_name():
        return TableResults.objects.all()[0].teamid.nameOfTeam
@register.inclusion_tag('table.html')
def show_all():
    choices = TableResults.objects.order_by('possition')
    return {'choices': choices}
