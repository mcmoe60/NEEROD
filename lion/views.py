from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
  <head>
    <title>max</title>
    <style>
      .google {
        color: yellow;
        text-align: center;
        font-size: 30px;
      }
      .input,
      .search {
        text-align: center;
        width: 600px;
        margin-left: auto;
        margin-right: 200px;
        height: 50px;
        border-radius: 10px;
      }
      .gmail,
      .e {
        text-align: right;
        margin-right: 20px;
        font-family: roboto;
        font-size: 18px;
        margin-top: 15px;
      }
    </style>
  </head>

  <body>
    <div class="gmail">Gmail Images <span class="e">e</span></div>

    <h1 class="google">Google</h1>

    <div class="search">
      <input
        class="input"
        type="text"
        placeholder="Search Google or type a URL"
      />
    </div>
  </body>
</html>""")