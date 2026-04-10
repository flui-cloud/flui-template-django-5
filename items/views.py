"""Views for the Flui demo Django app."""

import os
from datetime import datetime, timezone

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import store
from .serializers import ItemSerializer

_START_TIME = datetime.now(timezone.utc)


def home(_request):
    """Render the demo homepage."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{settings.APP_NAME}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0a0a0f; color: #e8e8ed; min-height: 100vh;
    }}
    a {{ color: #4f9eff; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .page {{ max-width: 800px; margin: 0 auto; padding: 4rem 2rem; }}
    .badge {{
      display: inline-block; padding: 0.4rem 0.9rem; border-radius: 999px;
      background: linear-gradient(135deg, #4f9eff, #a855f7); color: #fff;
      font-size: 0.8rem; font-weight: 600; margin-bottom: 1.5rem;
    }}
    h1 {{ font-size: 2.5rem; margin-bottom: 0.5rem; }}
    .subtitle {{ color: #888; margin-bottom: 2rem; }}
    .card {{
      background: #15151c; border: 1px solid #2a2a35; border-radius: 12px;
      padding: 1.5rem; margin-bottom: 2rem;
    }}
    .card h2 {{ font-size: 1.2rem; margin-bottom: 1rem; }}
    ul {{ list-style: none; display: grid; gap: 0.5rem; }}
    code {{
      display: inline-block; background: #2a2a35; color: #4f9eff;
      padding: 0.1rem 0.4rem; border-radius: 4px; font-size: 0.75rem;
      font-weight: 600; margin-right: 0.4rem;
    }}
    footer {{
      margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid #2a2a35;
      color: #666; font-size: 0.85rem; text-align: center;
    }}
  </style>
</head>
<body>
  <main class="page">
    <div class="badge">🚀 Flui Demo Application</div>
    <h1>{settings.APP_NAME}</h1>
    <p class="subtitle">Django 5 · DRF · drf-spectacular · v{settings.APP_VERSION}</p>
    <section class="card">
      <h2>API Endpoints</h2>
      <ul>
        <li><code>GET</code> <a href="/health/">/health/</a> — health</li>
        <li><code>GET</code> <a href="/items/">/items/</a> — list items</li>
        <li><code>POST</code> /items/ — create item</li>
        <li><code>GET</code> <a href="/api/openapi/">/api/openapi/</a> — spec</li>
        <li><code>GET</code> <a href="/docs/">/docs/</a> — Swagger UI</li>
      </ul>
    </section>
    <footer>Powered by <a href="https://flui.cloud">Flui</a></footer>
  </main>
</body>
</html>"""
    return HttpResponse(html, content_type='text/html; charset=utf-8')


def health(_request):
    """Health check endpoint."""
    uptime = int((datetime.now(timezone.utc) - _START_TIME).total_seconds())
    return JsonResponse({
        'status': 'ok',
        'appName': settings.APP_NAME,
        'version': settings.APP_VERSION,
        'uptime': uptime,
        'timestamp': datetime.now(timezone.utc).isoformat(),
    })


class ItemListCreateView(APIView):
    """List and create items."""

    @extend_schema(
        summary='List items',
        responses={200: ItemSerializer(many=True)},
    )
    def get(self, _request):
        return Response({'items': store.list_items()})

    @extend_schema(
        summary='Create item',
        request=ItemSerializer,
        responses={201: ItemSerializer},
    )
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = store.create_item(
            serializer.validated_data['name'],
            serializer.validated_data['description'],
        )
        return Response(item, status=status.HTTP_201_CREATED)


class ItemDetailView(APIView):
    """Get and delete a single item."""

    @extend_schema(
        summary='Get item by ID',
        responses={200: ItemSerializer, 404: OpenApiResponse(description='Not found')},
    )
    def get(self, _request, pk):
        item = store.get_item(pk)
        if not item:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(item)

    @extend_schema(
        summary='Delete item by ID',
        responses={200: OpenApiResponse(description='Deleted')},
    )
    def delete(self, _request, pk):
        if not store.delete_item(pk):
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'deleted': True})
