# blog_posts/views.py
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from mycompanyblog import db
from mycompanyblog.models import BlogPost
from mycompanyblog.blog_posts.forms import BlogPostForm
from mycompanyblog.users.picture_handler import add_post_pic

blog_posts = Blueprint('blog_posts', __name__)

# CREATE
@blog_posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        username = current_user.username
        title = form.title.data
        pic = add_post_pic(form.picture.data, title)

        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id,
                             post_image=pic,
                             price=form.price.data)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)

# Blog Post(VIEW)
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', post_image=blog_post.post_image, title=blog_post.title, date=blog_post.date, post=blog_post, price=blog_post.price)



# UPDATE
@blog_posts.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post.price = form.price.data
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        if form.picture.data != None:
            pic = add_post_pic(form.picture.data, blog_post.title)
            blog_post.post_image = pic
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post_id))

    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', title='Updating',form=form)


# DELETE
@blog_posts.route('/<int:blog_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))