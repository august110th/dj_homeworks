from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def pasta_view (request):
    servings = request.GET.get("servings", 1)
    context = {
        'recipe': {
            'макароны, г': 0.3*int(servings),
            'сыр, г': 0.05*int(servings),
        },
    }

    return render(request, "calculator/index.html", context)


def omlet_view(request):
    servings = request.GET.get("servings", 1)
    context = {
        'recipe': {
            'яйца, шт': 2*int(servings),
            'молоко, л': 0.1*int(servings),
            'соль, ч.л.': 0.5*int(servings),
        },
    }

    return render(request, "calculator/index.html", context)


def buter_view(request):
    servings = request.GET.get("servings", 1)
    context = {
        'recipe': {
            'хлеб, ломтик': 1*int(servings),
            'колбаса, ломтик': 1*int(servings),
            'сыр, ломтик': 1*int(servings),
            'помидор, ломтик': 1*int(servings),
        },
    }

    return render(request, "calculator/index.html", context)

def home_view(request):
    context = {'new_dict': DATA}
    return render(request, 'calculator/home.html', context)