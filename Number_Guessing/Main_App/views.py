from django.shortcuts import render, redirect
import random

def guess_number(request):
    if 'remaining_chances' not in request.session:
        # Initialize the remaining chances if it's not already set
        request.session['remaining_chances'] = 10

    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        number = request.session['number']
        result = None

        if guess == number:
            result = 'Congratulations! You guessed the number correctly. The number was {}'.format(number)
            request.session['remaining_chances'] = 0  # Set remaining chances to 0 to end the game
        elif guess > number:
            result = 'The number is smaller than your guess.'
        else:
            result = 'The number is greater than your guess.'

        request.session['remaining_chances'] -= 1

        if request.session['remaining_chances'] == 0:
            # Game over, out of chances
            result = 'Game over! You used all your chances. The number was {}'.format(number)
            number = None

    else:
        # Generate a new random number if it's a GET request or after a win
        number = random.randint(0, 999)
        request.session['number'] = number
        result = None

    context = {'number': number, 'result': result, 'remaining_chances': request.session['remaining_chances']}
    return render(request, 'guess_number.html', context)

def restart_game(request):
    request.session['remaining_chances'] = 10
    return redirect('guess_number')




def contact(request):
    # Add your contact logic here
    return render(request, 'contact.html')


def aboutus(request):
    # Add your contact logic here
    return render(request, 'aboutus.html')