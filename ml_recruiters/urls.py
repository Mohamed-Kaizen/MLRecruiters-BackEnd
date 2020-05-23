"""
ml_recruiters URL Configuration
"""
from dj_rest_auth.registration.views import VerifyEmailView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="MLRecruiters API",
        default_version="v1",
        description="""
        Every person needs help from other professionals be it electricians, plumbers, mechanics or any other.
         This project is a quick and easy way for people(recruiters)
         to connect with skilled people who think are a good fit and hire them""",
        contact=openapi.Contact(email="@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path(
        ".well-known/security.txt",
        TemplateView.as_view(template_name="security.txt", content_type="text/plain",),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain",),
    ),
    re_path(
        r"api/users/register/(?P<key>[-:\w]+)/",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("api/users/", include("users.urls")),
    path("api/users/", include("dj_rest_auth.urls")),
    path("api/users/register/", include("dj_rest_auth.registration.urls")),
    path("api/job/", include("jobs.urls")),
    re_path(
        r"^docs(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
