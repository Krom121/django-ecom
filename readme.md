# Purpose Of Application

The purpose of this website is to build a mordren ecommerce website that has plenty of space and very easy to use for the end user. The website has also been made responsive to industry standards.

## Features

    * Users can buy items from the shop without having to sign. up

    * Users can login and logout.

    * Users can read blogs.

    * Users can add or remove items from their cart.

    * Users can view product details.

    * Users can contact the company.

## Tech Used For This Website

    * Django was used as the primary framework.

    * Html 5 was used to structure the website pages.

    * CSS used for styling the website.

    * Bootstrap was used for layout, classes and basic components.

    * SQLite was used for a database.

## From Development To Production

I decided to build a ecommerce website, to chanallage myself to build a mordern website that was easy to use and only displayed the most relevent information to the end user. Without having to bombard the user with loads of breadcrumbs to get the user to impluse buy. I wanted to build a website that was sleak.

The design process was simple pick three main colours for the website, one light color for the background , one color for the font and one darker color for using in linear gradients. This would ensure the website would keep simple design flow and would be plesent to the eyes of the end user.

The colors that where pick dont shourd the text, but enhance the users readablity.

The layout again was to be simple not only for creating the space needed for a mordern design, Giving the content room to breathe, the content will be more readable/understandable for the user.

The file architecture for the website was split into 7 apps this will allow for other developers and myself to update the website with ease.

**Pages App:** Which holds all generic web pages, views, models and urls for example the index/landing page of the website.

**Blog App:** which has all the web pages for building a community for the shop. Blogs, Views, models and urls.

**Shop App:** This app is responsible for displaying the products to the end user. Products, models, views and urls.

**Orders App:** Responsiblee for handling all the users orders of the products.

**Cart App:** Responsible for displaying product in the checkout prier to payment.

**Payment App:** Responsible for handling the payment process.

**Users App:** Responsible for registering users, logging in users, logging out users and users profiles.

As the file structure suggest this website would very manageable for myself or other developers. Would have good scalability for future updates.

## Unit Testing

**Manual Testing:**

All forms where tested when built, before saving data to the database. When the python logic was add to save the data to the database, I test the forms again and queried the database using python shell.To known that the user information was implemented correctly.

Once this was done i added the form errors for validation. Then re-tested the forms to see the validation in place. Flash messages where used to inform the user of what is happening.

## Testing.py

```python  
class TestViews(TestCase):

    def test_product_list_GET(self):
        client = Client()
        response = client.get(reverse('shop:product_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')


class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolves(self):
        url = reverse('blog:post_list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

class TestUrls(SimpleTestCase):

        def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

        def test_contact_url_is_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

        def test_product_list_url_is_resolves(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func, product_list)

class TestViews(TestCase):

        def test_product_list_GET(self):
        client = Client()
        response = client.get(reverse('shop:product_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

```
