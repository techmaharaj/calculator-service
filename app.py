from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

class Calculator:
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

def validate_numbers(a, b):
    """Validate input parameters"""
    try:
        num_a = float(a)
        num_b = float(b)
        return num_a, num_b
    except (ValueError, TypeError):
        raise ValueError("Invalid input: both parameters must be numbers")

@app.route('/')
def index():
    """Serve the calculator UI"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "calculator"})

@app.route('/add')
def add():
    """Addition endpoint: /add?a=5&b=3"""
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({"error": "Missing parameters. Usage: /add?a=5&b=3"}), 400
            
        num_a, num_b = validate_numbers(a, b)
        result = Calculator.add(num_a, num_b)
        
        return jsonify({
            "operation": "addition",
            "a": num_a,
            "b": num_b,
            "result": result
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Addition error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/subtract')
def subtract():
    """Subtraction endpoint: /subtract?a=5&b=3"""
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({"error": "Missing parameters. Usage: /subtract?a=5&b=3"}), 400
            
        num_a, num_b = validate_numbers(a, b)
        result = Calculator.subtract(num_a, num_b)
        
        return jsonify({
            "operation": "subtraction",
            "a": num_a,
            "b": num_b,
            "result": result
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Subtraction error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/multiply')
def multiply():
    """Multiplication endpoint: /multiply?a=5&b=3"""
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({"error": "Missing parameters. Usage: /multiply?a=5&b=3"}), 400
            
        num_a, num_b = validate_numbers(a, b)
        result = Calculator.multiply(num_a, num_b)
        
        return jsonify({
            "operation": "multiplication",
            "a": num_a,
            "b": num_b,
            "result": result
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Multiplication error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/divide')
def divide():
    """Division endpoint: /divide?a=10&b=2"""
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({"error": "Missing parameters. Usage: /divide?a=10&b=2"}), 400
            
        num_a, num_b = validate_numbers(a, b)
        result = Calculator.divide(num_a, num_b)
        
        return jsonify({
            "operation": "division",
            "a": num_a,
            "b": num_b,
            "result": result
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Division error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/calculate', methods=['POST'])
def calculate():
    """General calculation endpoint for UI"""
    try:
        data = request.get_json()
        
        if not data or 'expression' not in data:
            return jsonify({"error": "Missing expression in request body"}), 400
            
        expression = data['expression']
        
        # Basic expression evaluation (secure for demo)
        # In production, use a proper math parser
        try:
            # Only allow basic math operations
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
                
            result = eval(expression)
            return jsonify({
                "expression": expression,
                "result": result
            })
        except ZeroDivisionError:
            return jsonify({"error": "Division by zero"}), 400
        except:
            return jsonify({"error": "Invalid expression"}), 400
            
    except Exception as e:
        app.logger.error(f"Calculate error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)