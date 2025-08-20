let currentInput = '0';
let expression = '';
let shouldResetDisplay = false;

const display = document.getElementById('display');
const expressionDiv = document.getElementById('expression');

function updateDisplay() {
    display.value = currentInput;
    expressionDiv.textContent = expression;
}

function appendNumber(num) {
    if (shouldResetDisplay) {
        currentInput = '';
        shouldResetDisplay = false;
    }
    
    if (currentInput === '0') {
        currentInput = num;
    } else {
        currentInput += num;
    }
    updateDisplay();
}

function appendDecimal() {
    if (shouldResetDisplay) {
        currentInput = '0';
        shouldResetDisplay = false;
    }
    
    if (!currentInput.includes('.')) {
        currentInput += '.';
    }
    updateDisplay();
}

function appendOperator(operator) {
    if (expression && !shouldResetDisplay) {
        calculate();
    }
    
    expression = currentInput + ' ' + operator + ' ';
    shouldResetDisplay = true;
    updateDisplay();
}

function clearAll() {
    currentInput = '0';
    expression = '';
    shouldResetDisplay = false;
    display.classList.remove('error');
    updateDisplay();
}

function clearEntry() {
    currentInput = '0';
    updateDisplay();
}

function backspace() {
    if (currentInput.length > 1) {
        currentInput = currentInput.slice(0, -1);
    } else {
        currentInput = '0';
    }
    updateDisplay();
}

async function calculate() {
    if (!expression) return;
    
    const fullExpression = expression + currentInput;
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: fullExpression })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            currentInput = data.result.toString();
            expression = '';
            shouldResetDisplay = true;
            display.classList.remove('error');
        } else {
            currentInput = 'Error';
            display.classList.add('error');
            console.error('Calculation error:', data.error);
        }
    } catch (error) {
        currentInput = 'Error';
        display.classList.add('error');
        console.error('Network error:', error);
    }
    
    updateDisplay();
}

// Keyboard support
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    if (key >= '0' && key <= '9') {
        appendNumber(key);
    } else if (key === '.') {
        appendDecimal();
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        appendOperator(key);
    } else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    } else if (key === 'Escape') {
        clearAll();
    } else if (key === 'Delete') {
        clearEntry();
    } else if (key === 'Backspace') {
        backspace();
    }
});

// Initialize display
updateDisplay();