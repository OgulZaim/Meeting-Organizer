from flask import Flask, request, render_template, redirect

app = Flask(__name__)

meetings = {}  # Toplantıları depolamak için sözlük kullanımı

@app.route('/create', methods=['GET', 'POST'])
def create_meeting():
    if request.method == 'POST':
        meeting_data = {
            'meeting_subject': request.form['meeting_subject'],
            'date': request.form['date'],
            'start_time': request.form['start_time'],
            'end_time': request.form['end_time'],
            'participants': request.form['participants']
        }
        # You can generate a unique meeting_id (e.g., using a timestamp or a UUID).
        # For example: meeting_id = str(uuid.uuid4())
        # Add the meeting to your storage with a unique ID.
        # Here, we'll use a simple numeric ID for demonstration purposes.
        meetings[len(meetings) + 1] = meeting_data
        return redirect('/list')  # Form doldurulunca liste sayfasına yönlendirmek için
    return render_template('register.html')

@app.route('/update/<int:meeting_id>', methods=['GET', 'POST'])
def update_meeting(meeting_id):
    if request.method == 'POST':
        if meeting_id in meetings:
            meeting_data = {
                'meeting_subject': request.form['meeting_subject'],
                'date': request.form['date'],
                'start_time': request.form['start_time'],
                'end_time': request.form['end_time'],
                'participants': request.form['participants']
            }
            # Bilgiler güncellendikten sonra toplantı bilgileri de güncellenir
            meetings[meeting_id] = meeting_data
            return redirect('/list')  # Toplantı bilgileri güncellendikten sonra liste sayfasına yöndendirmek için
        # Toplantı ID'si olmadığı durum için
        return "Meeting not found."
    meeting = meetings.get(meeting_id)
    return render_template('update.html', meeting=meeting, meeting_id=meeting_id)

@app.route('/list')
def list_meetings():
    # Meetings sözlüğünü görüntülemek için sözlükler listesine dönüştürmek için
    meeting_details = [{'meeting_id': k, **v} for k, v in meetings.items()]
    return render_template('list.html', meetings=meeting_details)

@app.route('/delete/<int:meeting_id>', methods=['POST'])
def delete_meeting(meeting_id):
    if meeting_id in meetings:
        # ID'si girilen toplantıyı silmek için
        del meetings[meeting_id]
        return redirect('/list')  # Toplantı silindikten sonra liste sayfasına yönlendirmek için
    # Toplantı ID'si olmadığında
    return "Meeting not found."

if __name__ == '__main__':
    app.run(debug=True)
