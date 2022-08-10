from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<CommissionsGrid>:
    cols: 3
    spacing: 10
    padding: 10


<CommissionCard>:
    size_hint: 1, 1
    orientation: 'vertical'
    padding: 10

    AsyncImage:
        size_hint: 1, 2
        source: root.image_url
    
    MDLabel:
        size_hint: 1, 1
        text: root.title
        font_style: 'Subtitle1'
        
    MDSeparator:
        size_hint: 1, None
    
    MDLabel:
        size_hint: 1, 1
        text: root.description
        font_style: 'Caption'


Screen:

    MDNavigationLayout:
    
        ScreenManager:
            id: screen_manager
        
            Screen:
            
                BoxLayout:
                    orientation: 'vertical'
                    spacing: 10
                    
                    MDToolbar:
                        title: 'Service Tasks'
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        
                    MDTextField:
                        hint_text: 'Search'
                        mode: 'rectangle'
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        size_hint: 0.5, None
                        padding: '12dp'
                        on_text: app.search(self.text)
                        icon_right: 'magnify'
                            
                    CommissionsGrid:
                        id: commissions_grid
                    
        
        MDNavigationDrawer:
            id: nav_drawer
        
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                orientation: 'vertical'
                padding: 20
                spacing: 15
            
                MDLabel:
                    text: 'Service Tasks'
                    font_style: 'Body1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: app.version
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDSeparator:
                
                Widget:
                    size_hint_y: 1
'''


class Commission:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url


class CommissionCard(MDCard):
    title, description, image_url = \
        StringProperty(), StringProperty(), StringProperty()

    def __init__(self, commission, **kwargs):
        super().__init__(**kwargs)
        self.title = commission.title
        self.description = commission.description
        self.image_url = commission.image_url


class CommissionsGrid(GridLayout):
    def render_commissions(self, commissions=(
            Commission(
                'Service Task 1',
                'Description of Service Task 1',
                'https://picsum.photos/200'
            ),
            Commission(
                'Service Task 2',
                'Description of Service Task 2',
                'https://picsum.photos/200'
            ),
            Commission(
                'Service Task 3',
                'Description of Service Task 3',
                'https://picsum.photos/200'
            ),
            Commission(
                'Service Task 4',
                'Description of Service Task 4',
                'https://picsum.photos/200'
            ),
            Commission(
                'Service Task 5',
                'Description of Service Task 5',
                'https://picsum.photos/200'
            )
    ), search_key=''):
        filtered_commissions = filter(
            lambda c:
                search_key.lower() in c.title.lower(),
            commissions
        ) if search_key else commissions
        for commission in filtered_commissions:
            self.add_widget(CommissionCard(commission))


class ContentNavigationDrawer(BoxLayout):
    pass


class MainApp(MDApp):
    version = '0.0.2'

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.commissions_grid.render_commissions()

    def search(self, search_key):
        commissions_grid = self.root.ids.commissions_grid
        commissions_grid.clear_widgets()
        commissions_grid.render_commissions(search_key=search_key)


def main():
    MainApp().run()


__all__ = ['main']


if __name__ == '__main__':
    main()
