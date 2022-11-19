from typing import TYPE_CHECKING

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse, PlainTextResponse, Response
from starlette.status import HTTP_204_NO_CONTENT

import test_data

if TYPE_CHECKING:
    from test_frameworks import EndpointSpec


app = Starlette()

# plaintext response


@app.route("/async-plaintext-6k")
async def async_plaintext_6k(request: Request) -> PlainTextResponse:
    return PlainTextResponse(test_data.TEXT_6k)


@app.route("/sync-plaintext-6k")
def sync_plaintext_6k(request: Request) -> PlainTextResponse:
    return PlainTextResponse(test_data.TEXT_6k)


@app.route("/async-plaintext-70k")
async def async_plaintext_70k(request: Request) -> PlainTextResponse:
    return PlainTextResponse(test_data.TEXT_70k)


@app.route("/sync-plaintext-70k")
def sync_plaintext_70k(request: Request) -> PlainTextResponse:
    return PlainTextResponse(test_data.TEXT_70k)


# JSON response


@app.route("/async-json-2k")
async def async_json_2k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_2K)


@app.route("/sync-json-2k")
def sync_json_2k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_2K)


@app.route("/async-json-10k")
async def async_json_10k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_10K)


@app.route("/sync-json-10k")
def sync_json_10k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_10K)


@app.route("/async-json-450k")
async def async_json_450k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_450K)


@app.route("/sync-json-450k")
def sync_json_450k(request: Request) -> JSONResponse:
    return JSONResponse(test_data.JSON_450K)


# params


@app.route("/async-no-params")
async def async_no_params(request: Request) -> Response:
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-no-params")
def sync_no_params(request: Request) -> Response:
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/async-path-params/{first:int}")
async def async_path_params(request: Request) -> Response:
    int(request.path_params["first"])
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-path-params/{first:int}")
def sync_path_params(request: Request) -> Response:
    int(request.path_params["first"])
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/async-query-param")
async def async_query_params(request: Request) -> Response:
    int(request.query_params["first"])
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-query-param")
def sync_query_params(request: Request) -> Response:
    int(request.query_params["first"])
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/async-mixed-params/{second:int}")
async def async_mixed_params(request: Request) -> Response:
    int(request.query_params["first"])
    request.path_params["second"]
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-mixed-params/{second:int}")
def sync_mixed_params(request: Request) -> Response:
    int(request.query_params["first"])
    request.path_params["second"]
    return Response(status_code=HTTP_204_NO_CONTENT)


# headers


@app.route("/async-request-headers")
async def async_request_headers(request: Request) -> Response:
    header_dict = {}
    for header_name, header_value in request.headers.items():
        header_dict[header_name] = header_value
    request.headers.getlist("header_1")
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-request-headers")
def sync_request_headers(request: Request) -> Response:
    header_dict = {}
    for header_name, header_value in request.headers.items():
        header_dict[header_name] = header_value
    request.headers.getlist("header_1")
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/async-response-headers")
async def async_response_headers(request: Request) -> Response:
    return Response(status_code=HTTP_204_NO_CONTENT, headers=test_data.RESPONSE_HEADERS)


@app.route("/sync-response-headers")
def sync_response_headers(request: Request) -> Response:
    return Response(status_code=HTTP_204_NO_CONTENT, headers=test_data.RESPONSE_HEADERS)


# cookies


@app.route("/async-request-cookies")
async def async_request_cookies(request: Request) -> Response:
    cookie_dict = {}
    for cookie_name, cookie_value in request.cookies.items():
        cookie_dict[cookie_name] = cookie_value
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-request-cookies")
def sync_request_cookies(request: Request) -> Response:
    cookie_dict = {}
    for cookie_name, cookie_value in request.cookies.items():
        cookie_dict[cookie_name] = cookie_value
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/async-response-cookies")
async def async_response_cookies(request: Request) -> Response:
    res = Response(status_code=HTTP_204_NO_CONTENT)
    for key, value in test_data.RESPONSE_COOKIES.items():
        res.set_cookie(key, value)
    return res


@app.route("/sync-response-cookies")
def sync_response_cookies(request: Request) -> Response:
    res = Response(status_code=HTTP_204_NO_CONTENT)
    for key, value in test_data.RESPONSE_COOKIES.items():
        res.set_cookie(key, value)
    return res


# url


@app.route("/async-url-access")
async def async_url_access(request: Request) -> Response:
    scheme = request.url.scheme  # noqa: F841
    netloc = request.url.netloc  # noqa: F841
    path = request.url.path  # noqa: F841
    fragment = request.url.fragment  # noqa: F841
    query = request.url.query  # noqa: F841
    username = request.url.username  # noqa: F841
    password = request.url.password  # noqa: F841
    port = request.url.port  # noqa: F841
    hostname = request.url.hostname  # noqa: F841
    for param, value in request.query_params.items():  # noqa: B007
        pass
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.route("/sync-url-access")
def sync_url_access(request: Request) -> Response:
    scheme = request.url.scheme  # noqa: F841
    netloc = request.url.netloc  # noqa: F841
    path = request.url.path  # noqa: F841
    fragment = request.url.fragment  # noqa: F841
    query = request.url.query  # noqa: F841
    username = request.url.username  # noqa: F841
    password = request.url.password  # noqa: F841
    port = request.url.port  # noqa: F841
    hostname = request.url.hostname  # noqa: F841
    for param, value in request.query_params.items():  # noqa: B007
        pass
    return Response(status_code=HTTP_204_NO_CONTENT)


# files


@app.route("/async-file-response-100B")
async def async_file_response_100b(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_100B, filename="response_file")


@app.route("/async-file-response-50K")
async def async_file_response_50k(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_50K, filename="response_file")


@app.route("/async-file-response-1K")
async def async_file_response_1k(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_1K, filename="response_file")


@app.route("/async-file-response-1M")
async def async_file_response_1m(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_1M, filename="response_file")


@app.route("/sync-file-response-100B")
def sync_file_response_100b(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_100B, filename="response_file")


@app.route("/sync-file-response-50K")
def sync_file_response_50k(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_50K, filename="response_file")


@app.route("/sync-file-response-1K")
def sync_file_response_1k(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_1K, filename="response_file")


@app.route("/sync-file-response-1M")
def sync_file_response_1m(request: Request) -> FileResponse:
    return FileResponse(path=test_data.RESPONSE_FILE_1M, filename="response_file")


def run_spec_test(url: str, spec: "EndpointSpec") -> None:
    from starlette.testclient import TestClient

    with TestClient(app=app) as client:
        res = client.get(url, **spec.get("request", {}))
        assert res.status_code == spec["result"]["status_code"]
        if expect_bytes := spec["result"].get("bytes"):
            assert expect_bytes == res.content
        if expect_text := spec["result"].get("text"):
            assert expect_text == res.text
        if expect_json := spec["result"].get("json"):
            assert res.json() == expect_json
