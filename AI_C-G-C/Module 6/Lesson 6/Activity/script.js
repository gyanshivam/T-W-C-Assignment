/*
    FUNCTIONING OF THE CALCULATOR

    This JavaScript file gives behaviour to the
    calculator created using HTML and CSS.

    The main tasks are:

    1. Read values from the calculator display.
    2. Write values to the calculator display.
    3. Add numbers when number buttons are clicked.
    4. Store mathematical operations.
    5. Perform calculations when "=" is clicked.
    6. Clear the calculator.
    7. Remove the last digit using CE.
    8. Handle percentage calculations.
*/

/*
    ----------------------------------------------------
    1. GET HISTORY
    ----------------------------------------------------

    The history area contains the mathematical
    expression being created.

    Example:

        25+10

    document.getElementById() searches the HTML document
    for an element having the specified id.

    innerText returns the visible text inside that element.
*/
function getHistory() {
  return document.getElementById('history-value').innerText
}

/*
    ----------------------------------------------------
    2. DISPLAY HISTORY
    ----------------------------------------------------

    This function receives some text and displays it
    inside the history section.

    Example:

        printHistory("25+10");

    will display:

        25+10
*/
function printHistory(value) {
  document.getElementById('history-value').innerText = value
}

/*
    ----------------------------------------------------
    3. GET CURRENT OUTPUT
    ----------------------------------------------------

    The output area contains the number currently
    being entered.

    Example:

        25

    or:

        1000
*/
function getOutput() {
  return document.getElementById('output-value').innerText
}

/*
    ----------------------------------------------------
    4. DISPLAY OUTPUT
    ----------------------------------------------------

    This function prints a number to the calculator.

    If the value is empty, we display nothing.

    Otherwise, getFormattedNumber() is used to make
    large numbers easier to read.

    Example:

        1000000

    becomes:

        1,000,000
*/
function printOutput(value) {
  if (value === '') {
    document.getElementById('output-value').innerText = ''
  } else {
    document.getElementById('output-value').innerText =
      getFormattedNumber(value)
  }
}

/*
    ----------------------------------------------------
    5. FORMAT NUMBERS
    ----------------------------------------------------

    toLocaleString("en-US") adds commas to numbers.

    Example:

        1000    -> 1,000
        250000  -> 250,000

    This is only for displaying the number.

    The actual mathematical value is still a number.
*/
function getFormattedNumber(value) {
  if (value === '-') {
    return ''
  }

  var number = Number(value)

  return number.toLocaleString('en-US')
}

/*
    ----------------------------------------------------
    6. REMOVE COMMAS
    ----------------------------------------------------

    The displayed number may contain commas.

    Example:

        "10,000"

    JavaScript should work with:

        10000

    replace() removes every comma.

    The regular expression /,/g means:

        ,
        g = every occurrence

    Number() then converts the resulting text
    back into a number.
*/
function reverseNumberFormat(value) {
  return Number(value.replace(/,/g, ''))
}

/*
    ----------------------------------------------------
    7. OPERATOR BUTTONS
    ----------------------------------------------------

    getElementsByClassName("operator") finds all
    elements having the class "operator".

    This includes:

        C
        CE
        %
        /
        *
        -
        +
        =

    The result is a collection of elements.
*/
var operators = document.getElementsByClassName('operator')

/*
    Loop through every operator button.

    addEventListener() tells JavaScript:

        "When this button is clicked,
         run this function."
*/
for (var i = 0; i < operators.length; i++) {
  operators[i].addEventListener('click', function () {
    /*
            "this" refers to the operator button
            that the user actually clicked.

            this.id gives us its id.

            Example:

                + button -> this.id is "+"
                - button -> this.id is "-"
                = button -> this.id is "="
        */

    /*
            ------------------------------------------------
            CLEAR BUTTON
            ------------------------------------------------

            C removes both the calculation history
            and current output.
        */
    if (this.id === 'clear') {
      printHistory('')
      printOutput('')

      return
    }

    /*
            ------------------------------------------------
            BACKSPACE / CE BUTTON
            ------------------------------------------------

            CE removes the last digit.

            Example:

                1234

            becomes:

                123
        */
    if (this.id === 'backspace') {
      var currentOutput = getOutput()

      /*
                If there is no number, there is
                nothing to delete.
            */
      if (currentOutput !== '') {
        /*
                    Remove commas before editing
                    the number.
                */
        var plainNumber = reverseNumberFormat(currentOutput).toString()

        /*
                    slice(0, -1) removes the final character.

                    Example:

                    "1234" -> "123"
                */
        plainNumber = plainNumber.slice(0, -1)

        printOutput(plainNumber)
      }

      return
    }

    /*
            ------------------------------------------------
            OTHER OPERATORS
            ------------------------------------------------

            At this point the button can be:

                %
                /
                *
                -
                +
                =
        */

    var output = getOutput()
    var history = getHistory()

    /*
            If the current output is empty but there
            is already an operator in history, remove
            the old operator before adding another one.

            Example:

                10 +

            User clicks -

            We want:

                10 -

            rather than:

                10 + -
        */
    if (output === '' && history !== '') {
      var lastCharacter = history.charAt(history.length - 1)

      if (isNaN(lastCharacter) && lastCharacter !== '%') {
        history = history.slice(0, history.length - 1)
      }
    }

    /*
            Continue only if there is something
            to calculate.
        */
    if (output !== '' || history !== '') {
      /*
                Convert formatted output back into
                a normal number.

                Example:

                    "1,000" -> 1000
            */
      if (output !== '') {
        output = reverseNumberFormat(output)
      }

      /*
                Add the current number to history.

                Example:

                    history = "25+"
                    output  = 10

                becomes:

                    "25+10"
            */
      history = history + output

      /*
                ------------------------------------------------
                EQUAL BUTTON
                ------------------------------------------------

                "=" means calculate the expression.
            */
      if (this.id === '=') {
        var answer = calculateExpression(history)

        printOutput(answer)

        /*
                    Clear history after displaying
                    the final answer.
                */
        printHistory('')
      } else {
        /*
                    For normal operators, add the
                    operator to the history.

                    Example:

                        25 + 10

                    The history becomes:

                        25+10+
                */
        history = history + this.id

        printHistory(history)

        /*
                    Clear output so the user can
                    enter the next number.
                */
        printOutput('')
      }
    }
  })
}

/*
    ----------------------------------------------------
    8. CALCULATE EXPRESSION
    ----------------------------------------------------

    Instead of using eval(), we process the expression
    ourselves.

    This keeps the calculator logic easier to understand
    and avoids executing arbitrary JavaScript code.
*/
function calculateExpression(expression) {
  /*
        Handle percentage.

        Example:

            50%

        becomes:

            0.5
    */
  expression = expression.replace(/(\d+(?:\.\d+)?)%/g, '($1/100)')

  /*
        Split the expression into numbers and operators.

        Example:

            "20+5*2"

        becomes pieces such as:

            20
            +
            5
            *
            2
    */
  var parts = expression.match(/(\d+(?:\.\d+)?)|[+\-*/]/g)

  if (!parts) {
    return ''
  }

  /*
        Start with the first number.
    */
  var total = Number(parts[0])

  /*
        Process each operator and the number
        immediately after it.
    */
  for (var i = 1; i < parts.length; i += 2) {
    var operator = parts[i]
    var nextNumber = Number(parts[i + 1])

    if (operator === '+') {
      total = total + nextNumber
    } else if (operator === '-') {
      total = total - nextNumber
    } else if (operator === '*') {
      total = total * nextNumber
    } else if (operator === '/') {
      /*
                Prevent division by zero.
            */
      if (nextNumber === 0) {
        return 'Error'
      }

      total = total / nextNumber
    }
  }

  /*
        Return the final result.
    */
  return total
}

/*
    ----------------------------------------------------
    9. NUMBER BUTTONS
    ----------------------------------------------------

    Find all buttons having the class "number".

    These are:

        0
        1
        2
        ...
        9
*/
var numbers = document.getElementsByClassName('number')

/*
    Add a click event to every number button.
*/
for (var j = 0; j < numbers.length; j++) {
  numbers[j].addEventListener('click', function () {
    /*
            Get whatever number is currently
            displayed.
        */
    var output = getOutput()

    /*
            If the display is empty, start with
            an empty string.
        */
    if (output === '') {
      output = ''
    } else {
      /*
                Remove commas before adding
                another digit.
            */
      output = reverseNumberFormat(output).toString()
    }

    /*
            this.id contains the number pressed.

            For example:

                Clicking button 7

                this.id = "7"
        */
    output = output + this.id

    /*
            Display the newly created number.
        */
    printOutput(output)
  })
}
