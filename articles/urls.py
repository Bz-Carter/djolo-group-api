from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import ( FileUploadView, CategoryGenericAPIView, TypeGenericAPIView,
PhotoGenericAPIView, VideoGenericAPIView, PropertyGenericAPIView, SpaceGenericAPIView,  PartnerGenericAPIView,
PublicCategoryGenericAPIView, PublicTypeGenericAPIView, PublicPhotoGenericAPIView, PublicVideoGenericAPIView,
PublicPropertyGenericAPIView, PublicSpaceGenericAPIView, PublicPartnerGenericAPIView
)

urlpatterns = [
    path('properties', PropertyGenericAPIView.as_view()),
    path('property', PublicPropertyGenericAPIView.as_view()),
    path('properties/<str:pk>', PropertyGenericAPIView.as_view()),
    path('property/<str:pk>', PublicPropertyGenericAPIView.as_view()),
    path('spaces', SpaceGenericAPIView.as_view()),
    path('space', PublicSpaceGenericAPIView.as_view()),
    path('spaces/<str:pk>', SpaceGenericAPIView.as_view()),
    path('space/<str:pk>', PublicSpaceGenericAPIView.as_view()),
    path('types', TypeGenericAPIView.as_view()),
    path('type', PublicTypeGenericAPIView.as_view()),
    path('types/<str:pk>', TypeGenericAPIView.as_view()),
    path('type/<str:pk>', PublicTypeGenericAPIView.as_view()),
    path('categories', CategoryGenericAPIView.as_view()),
    path('category', PublicCategoryGenericAPIView.as_view()),
    path('categories/<str:pk>', CategoryGenericAPIView.as_view()),
    path('category/<str:pk>', PublicCategoryGenericAPIView.as_view()),
    path('partners', PartnerGenericAPIView.as_view()),
    path('partner', PublicPartnerGenericAPIView.as_view()),
    path('partners/<str:pk>', PartnerGenericAPIView.as_view()),
    path('partner/<str:pk>', PublicPartnerGenericAPIView.as_view()),
    path('upload', FileUploadView.as_view()),
    path('videos', VideoGenericAPIView.as_view()),
    path('video', PublicVideoGenericAPIView.as_view()),
    path('videos/<str:pk>', VideoGenericAPIView.as_view()),
    path('video/<str:pk>', PublicVideoGenericAPIView.as_view()),
    path('photos', PhotoGenericAPIView.as_view()),
    path('photo', PublicPhotoGenericAPIView.as_view()),
    path('photos/<str:pk>', PhotoGenericAPIView.as_view()),
    path('photo/<str:pk>', PublicPhotoGenericAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)