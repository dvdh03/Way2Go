from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from langchain.prompts import PromptTemplate
import ollama
from langchain_ollama.llms import OllamaLLM
from datetime import datetime, timedelta  # Ensure no syntax errors here
from .models import ItineraryRequest

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('home2')
        else:
            messages.error(request, "There was an error in your form. Please try again.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return '/home2/'

def itineraries(request):
    return render(request, 'it.html') 

def home2_view(request):
    return render(request, 'home2.html')

def about(request):
    return render(request, 'ab.html')

def start(request):
    return render(request, 'start.html')

def plan(request):
    return render(request, 'plan.html')

@csrf_exempt
def generate_itinerary(request): 
    if request.method == "POST":
        # Check if the user is authenticated
        if request.user.is_authenticated:
            username = request.user.username  # Get the username if the user is authenticated
        else:
            # Redirect to login page or handle the case where user is not authenticated
            return redirect('login')  # Adjust the redirect to your login URL if needed
        
        # Extract user input from the POST request
        budget = request.POST.get("budget", "1000")
        climate = request.POST.get("climate", "moderate")
        interests = request.POST.getlist("interests")
        group_size = request.POST.get("group_size", "1")
        duration = request.POST.get("duration", "3")
        start_date = datetime.now().strftime("%Y-%m-%d")
        end_date = (datetime.now() + timedelta(days=int(duration))).strftime("%Y-%m-%d")

        # Prepare the query for the AI model
        query = f"""
        Create a travel itinerary based on the following details:
        Budget: ₹{budget}
        Climate Preference: {climate}
        Interests: {', '.join(interests)}
        Group Size: {group_size}
        Duration: {duration} days
        Start Date: {start_date}.
        """
        
        # Define the prompt template
        prompt_template = PromptTemplate(
            input_variables=["query"],
            template=""" 
            Create a travel itinerary from this input:
            {query}
            
            Structure the response as:
            
            Itinerary Details
            Destination: [Destination]
            
            Duration: [Duration]
            
            Start Date: [Start Date]
            
            End Date: [End Date]
            
            Description:
            
            [Detailed Description of the Itinerary]
            
            Highlights:
            
            [Highlight 1]
            [Highlight 2]
            [Highlight 3]
            
            Additional Notes: [Any extra notes regarding the itinerary]
            """
        )

        # Format the prompt with the user query
        final_prompt = prompt_template.format(query=query)

        # Initialize the Ollama model using LangChain
        ollama_model = OllamaLLM(model="llama3.2:3b")  # Use the correct model name

        # Generate the itinerary using the Ollama model
        response = ollama_model(final_prompt)

        # Save data to the database, including the username
        itinerary_request = ItineraryRequest(
            username=username,  # Store the username
            budget=budget,
            climate=climate,
            interests=",".join(interests),
            group_size=group_size,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            response=response
        )
        itinerary_request.save()

        # Render the structured itinerary on the response page
        context = {
            "itinerary": response
        }
        return render(request, "generate.html", context)
    else:
        return render(request, "ai.html")

def destinations(request):
    return render(request, 'st.html')

def ai(request):
    return render(request, 'ai.html')