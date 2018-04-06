# KATE
## Description

This repository is a Application software with Python and Django 2, this application contains a registry
of users with their respective annotations.

## Installation
Using Python3 and Django 2 preferably.

## Usage
```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/Kate.git [NAME APP] 
```
Follow the following steps and you're good to go! Important:


![alt text]


## Coding
### Views

```python
def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            #FIXME: import redirect
            return redirect('index')
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'guestbook/sign.html', context)
```

### Model

```python
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    #FIXME: Create a Special Method
    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/Kate. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).