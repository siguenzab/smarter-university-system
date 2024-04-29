from app.controllers.discussions_controller import DiscussionsController

def main():
    ctrl = DiscussionsController('discussions_test.json')
    ctrl.add_discussion("Discssion Title", "text", "user_01")
    ctrl.print_discussion_board()

if __name__ == "__main__":
    main()