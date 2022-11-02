from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short!", category='error')
        else:
            user_id = current_user.id
            new_note = Note(data=note, user_id=user_id)

            db.session.add(new_note)
            db.session.commit()

        

    return render_template("home.html", user=current_user)

@views.route('/<note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id)

    if note and note.user_id == current_user.id:
        note.delete()
        db.session.commit()
        return jsonify({})
    else:
        flash("This note not exist!", category='error')
        return redirect(url_for('views.home'))
    
