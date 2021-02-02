from bottle import run, post, request as bottle_request  # <--- we add bottle request

@post('/')
def main():
    data = bottle_request.json  # <--- extract all request data
    print(data)

    return


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)