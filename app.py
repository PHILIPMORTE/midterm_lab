from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def contact():
    return render_template('contact_form.html', form={}, errors=[])

@app.route('/submit', methods=['POST'])
def submit():
    errors = []
    form = request.form.to_dict(flat=False)

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    message = request.form.get('message', '').strip()
    subject = request.form.get('subject', '')
    other_subject = request.form.get('other_subject', '')
    preferred = request.form.getlist('preferred')  # Corrected here to use getlist
    agreement = request.form.get('agreement')

    if not name:
        errors.append("Name is required.")
    if not email:
        errors.append("Email is required.")
    if not phone.isdigit():
        errors.append("Phone number must be numeric.")
    if not message:
        errors.append("Message is required.")
    if not agreement:
        errors.append("You must agree to the terms and conditions.")

    final_subject = other_subject if subject == "Other" else subject

    if errors:
        return render_template("contact_form.html", form=request.form, errors=errors)

    return render_template("confirmation.html", name=name, email=email, phone=phone,
                           message=message, subject=final_subject, preferred=preferred,
                           agreement="Yes" if agreement else "No")

if __name__ == '__main__':
    app.run(debug=True)