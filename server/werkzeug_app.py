from werkzeug.wrappers import Request, Response

# This decorator turns this function into a WSGI application
@Request.application
def application(request):
    # Prints the client's IP in the terminal
    print(f'This web server is running at {request.remote_addr}')
    
    # Response that will show up in the browser
    return Response('A WSGI generated this response!', content_type='text/plain')

# Run the development server when this file is executed directly
if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple(
        hostname='localhost',   # Local machine
        port=5555,              # Port the server will run on
        application=application
    )
