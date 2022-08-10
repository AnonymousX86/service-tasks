from kivy import require as kivy_require
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

kivy_require('2.1.0')


class Commission:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url


class NoSearchResultsCard(MDCard):
    pass


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
        filtered_commissions: tuple[Commission] = tuple(filter(
            lambda c:
            search_key.lower() in c.title.lower(),
            commissions
        )) if search_key else commissions
        if not filtered_commissions:
            self.add_widget(NoSearchResultsCard())
        else:
            for commission in filtered_commissions:
                self.add_widget(CommissionCard(commission))


class ContentNavigationDrawer(BoxLayout):
    pass


class MainApp(MDApp):
    version = '0.0.2'

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
