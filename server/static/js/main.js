document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');
    const predictionText = document.getElementById('prediction-text');
    const submitBtn = document.getElementById('submit-btn');
    const loader = document.getElementById('loader');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Show loading state
        submitBtn.disabled = true;
        resultContainer.classList.add('hidden');
        loader.classList.remove('hidden');

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/api/v1/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();

            if (result.status === 'success') {
                predictionText.textContent = result.data.prediction.toLocaleString();
                resultContainer.classList.remove('hidden');
            } else {
                alert('Error: ' + (result.message || 'Failed to get prediction'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong. Please check if the server is running.');
        } finally {
            submitBtn.disabled = false;
            loader.classList.add('hidden');
        }
    });
});
