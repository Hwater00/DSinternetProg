from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post,Category

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

        self.user_james = User.objects.create_user(username='James',password='aomepassword')
        self.user_trump = User.objects.create_user(username='Trump', password='aomepassword')

        self.category_programming = Category.objects.creat(name='programming',slug='programming')
        self.category_culture = Category.objects.creat(name='culture', slug='culture')

        # 포스트게시물이 3개 존재
        self.post_001 = Post.objects.create(
            title='첫번째 포스트',
            content='Hello World!! We are the wrold',
            author=self.user_james,
            category=self.categroy_programming
        )
        self.post_002 = Post.objects.create(
            title='두번째 포스트',
            content='1등이 전부가 아니잖아요',
            author=self.user_trump,
            category=self.category_culture
        )
        self.post_003 = Post.objects.create(
            title='세번째 포스트',
            content='세번째 포스트',
            author=self.user_trump,

        )


    def navbar_test(self, soup):
        # 포스트 목록과 같은 네비게이션바가 있는가
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        logo=navbar.find('a',text='Internet Programmong')
        self.assertEqual(logo.attrs['href'],'/')
        home = navbar.find('a', text='Home')
        self.assertEqual(home.attrs['href'], '/')
        blog = navbar.find('a', text='Blog')
        self.assertEqual(blog.attrs['href'], '/blog/')
        about = navbar.find('a', text='About Me')
        self.assertEqual(about.attrs['href'], '/about_me/')

    def category_test(self,soup):
        category = soup.find('div' ,id='categories-card')
        self.assertIn('Categories',category.text)
        self.assertIn(f'{self.category_programming.name} ({self.category_programming.post_set.count()})',category.text)
        self.assertIn(f'{self.category_culture.name} ({self.category_culture.post_set.count()})', category.text)
        self.assertIn(f'미분류 (1)',category.text)

    def test_category_page(self):
        response = self.clinet.get(self.category_programming.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup)
        self.category_test(soup)
        self.assertIn(self.category_programming.name,soup.h1.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn(self.category_programming.name,main_area.text)
        self.assertIn(self.post_001.title,main_area.text)
        self.assertNotIn(self.post_002.title, main_area.text)
        self.assertNotIn(self.post_003.title, main_area.text)




    def test_post_list(self):
        self.assertEqual(Post.objects.count(), 3)
        #포스트 목록페이지를 가져온다
        response = self.client.get('/blog/')
        #정상적으로 페이지 로드
        self.assertEqual(response.status_code,200)
        #페이지 타이틀 '블로그'
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text,'Blog')
        #네비게이션 바 존재
        self.navbar_test(soup)
        self.category_test(soup)

         #타이틀 3
        main_area = soup.find('div', id='main-area')
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

        post_001_card= main_area.find('div',id='post-1')
        self.assertIn(self.post_001.title,  post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)

        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)

        post_003_card = main_area.find('div', id='post-3')
        self.assertIn(self.post_003.title, post_003_card.text)
        self.assertIn('미분류', post_003_card.text)

        self.assertIn(self.user_james.username.upper(),main_area.text)
        self.assertIn(self.user_trump.username.upper(), main_area.text)

        # 포스트가 하나도 없는 경우
        Post.objects.all().delete()
        self.assertEqual(Post.objects.count(), 0)
        # 포스트 목록페이지를 가져온다
        response = self.client.get('/blog/')
        # 정상적으로 페이지 로드
        self.assertEqual(response.status_code, 200)
        # 페이지 타이틀 '블로그'
        soup = BeautifulSoup(response.content, 'html.parser')

        # 적절한 안내 문구가 포함되어 있는지
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

    def test_post_detail(self):
        #포스트 하나


        #이 포스트의 url이
        self.assertEqual(self.post_001.get_absolute_url(), '/blog/1')

        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        #포스트 목록과 같은 네비게이션바가 있는가
        self.navbar_test(soup)
        self.category_test(soup)

        #포스트의 타이틀은 웹브라우저의 TITLE에 있는가
        self.assertIn(self.post_001.title, soup.title.text)
        #포스트 영역에도 있는가
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id="post-area")
        self.assertIn(self.post_001.title, post_area.text)
        self.assertIn(self.post_001.category.name, post_area.text)
        self.assertIn(self.post_001.content, post_area.text)

        self.assertIn(self.user_james.username.upper(), post_area.txt)



