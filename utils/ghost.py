import os
import json
import requests

from utils.auth import get_token


def create_post(title, tags: list[str], authors: list[str], markdown: str, status: str = "draft"):
    ghost_url = os.getenv('GHOST_URL')
    token = get_token()
    url = f"{ghost_url}/ghost/api/admin/posts/"
    headers = {'Authorization': 'Ghost {}'.format(token)}

    mobiledoc = {
        "version": '0.3.1',
        "markups": [],
        "atoms": [],
        "cards": [
            ["markdown", {"markdown": markdown}]
        ],
        "sections": [[10, 0]]
    }

    body = {'posts': [{
        'title': title,
        'tags': tags,
        'authors': authors,
        'status': status,
        'mobiledoc': json.dumps(mobiledoc)
    }]}

    response = requests.post(url, json=body, headers=headers)
    return response.json()["posts"][0]
