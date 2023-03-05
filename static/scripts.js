const form = document.querySelector('#autocomplete-form');
const promptInput = document.querySelector('#prompt');
const suggestionOutput = document.querySelector('#suggestion');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const prompt = promptInput.value;
    if (prompt.trim() === '') {
        suggestionOutput.innerHTML = 'Please enter some text.';
        return;
    }
    getSuggestion(prompt);
});

async function getSuggestion(prompt) {
    suggestionOutput.innerHTML = '';

    const params = new URLSearchParams({
        prompt: prompt
    });

    const response = await fetch(`/autocomplete?${params}`, {
        method: 'GET',
    });

    const data = await response.json();
    suggestionOutput.innerHTML = data.message;
}
