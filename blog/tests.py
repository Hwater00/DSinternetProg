from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

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

    def test_post_list(self):
        #포스트 목록페이지를 가져온다
        response = self.client.get('/blog/')
        #정상적으로 페이지 로드
        self.assertEqual(response.status_code,200)
        #페이지 타이틀 '블로그'
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text,'Blog')
        #네비게이션 바 존재
        self.navbar_test(soup)

        #포스트가 하나도 없는 경우
        self.assertEqual(Post.objects.count(),0)
        #적절한 안내 문구가 포함되어 있는지
        main_area=soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        #포스트게시물이 2개 존재
        post_001 = Post.objects.create(
            title='첫번째 포스트',
            content= 'Hello World!! We are the wrold',
        )
        post_002= Post.objects.create(
            title='두번째 포스트',
            content='1등이 전부가 아니잖아요',
        )
        self.assertEqual(Post.objects.count(),2)
        # 포스트 목록페이지를 가져온다
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        #타이틀 2
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

    def test_post_detail(self):
        #포스트 하나
        post_001 = Post.objects.create(
            title='첫번째 포스트',
            content='Hello World!! We are the wrold',
        )
        #이 포스트의 url이
        self.assertEqual(post_001.get_absolute_url(), '/blog/1')

        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        #포스트 목록과 같은 네비게이션바가 있는가
        self.navbar_test(soup)

        #포스트의 타이틀은 웹브라우저의 TITLE에 있는가
        self.assertIn(post_001.title, soup.title.text)
        #포스트 영역에도 있는가
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id="post-area")
        self.assertIn(post_001.title, post_area.text)
        self.assertIn(post_001.content, post_area.text)

