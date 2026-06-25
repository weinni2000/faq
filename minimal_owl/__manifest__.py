{
    "name": "demo",
    "author": "mytime.click",
    "category": "Uncategorized",
    "version": "18.0.1.1",
    "license": "AGPL-3",
    "depends": [
        "base",
        "website",
        "portal",
    ],
    "data": [
        "views/portal_extension.xml",
        "views/minimal_owl_template.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "minimal_owl/static/src/js/*.js",
            "minimal_owl/static/src/js/components/minimal_owl/**/*",
            "minimal_owl/static/src/lib/package/bootstrap.bundle.min.js",
        ],
    },
}
