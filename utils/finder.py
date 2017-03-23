import json




def star_finder(json_matrix):
    matrix = json.loads(json_matrix)
    matrix = map(
        lambda row: map(
            lambda el: {
                'signal': el,
                'visited': False
            }
        )
    )
    for i in xrange():
        pass


def star_definition(starts, matrix, i, j):
