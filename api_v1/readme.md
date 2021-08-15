# Api V1

This api is public.

## Endpoint

### Article

#### Get list
Route: https://redcraft.org/api/v1/\<language\>/articles <br>
Method: GET <br>
Query parametres:
- current_page: 
    - integer >= 0
    - optional, default = 1
- per_page:
    - integer >= [1, 100]
    - optional, default = 10

Response samples: 
```json
{
    "nb_page": 4,
    "current_page": 0,
    "nb_article": 89,
    "list": [
        {
            "id": 89,
            "title": "A good test",
            "overview": "Look my good test",
            "category": "fr",
            "link": {
                "article": "https://redcraft.org/api/v1/fr/article/89/fr/a-good-test",
            }
        },
        ...
    ],
    "_link": {
        "next_page": "https://redcraft.org/api/v1/fr/articles?page=1&per_page=15",
        "prev_page": "false"
    },
}
```

#### Get article
Route: https://redcraft.org/api/v1/{language}/article/{id}/{slug} <br>
Method: GET <br>
Query parametres:
- current_page: 
    - integer >= 0
    - optional, default = 1
- per_page:
    - integer >= [1, 100]
    - optional, default = 10

Response samples: 
```json
{
    "id": 89,
    "title": "Un bon test",
    "overview": "Regarde mon beau test",
    "text": "Un super text de test",
    "category": "redstone",
    "link": {
        "article": "https://redcraft.org/api/v1/article/89/fr/un-bon-test",
    }
}
```


#### Get new articles
Route : https://redcraft.org/api/v1/\<language\>/articles/newa <br>
Method: GET <br>
Query parametres:
- nb:
    - integer [1, 15]
    - optional

Response samples:
```json
{
    "list": [
        {
            "id": 89,
            "title": "A good test",
            "overview": "Look my good test",
            "path_img": "public/test/test.png",
            "category": "redstone",
            "link": {
                "article": "https://redcraft.org/api/v1/article/89/fr/a-good-test",
            }
        },
        ...
    ]
}
```