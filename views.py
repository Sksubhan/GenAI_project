from django.shortcuts import render
import google.generativeai as genai
import markdown


def home(request):
    if request.method == 'POST':
        # Get the user input from the POST request
        a = request.POST["txt"]

        # Configure the Generative AI API
        genai.configure(api_key="API key")  # < --  API from gemini AI.
        model = genai.GenerativeModel("gemini-pro")

        # Generate content using the AI model
        response = model.generate_content(f"{a}")

        # Get the text response and format it as a string
        markdown_text = response.text.replace('•', '*')
        text = markdown.markdown(markdown_text)

        # Render the response in the 'index.html' template
        return render(request, 'a.html', {'text': text, 'a': a})

    # If it's a GET request, simply render the empty form
    return render(request, 'a.html')
