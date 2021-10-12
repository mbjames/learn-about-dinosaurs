import banner
import menu


def start():
    banner.print_banner()

    menu.main_menu()

    answer = input('\n > ').lower()

    if answer == 'q':
        exit()

    elif answer == '1':
        print('\n Triceratops was a plant-eater with specialised teeth for cutting')
        print(' and slicing and a huge stomach for digesting tough plant matter.')
        print(' It would have used its horns for defending itself from predators like Tyrannosaurus.')

        start()

    elif answer == '2':
        print('\n This slow-moving plant-eater used spikes on its tail to fend off would-be predators.')
        print(' The jury is still out on what the spiny plates on its back were used for.')

        start()

    elif answer == '3':
        print('\n An infamous meat-eating predator.')
        print(' Look at the evidence as to whether Tyrannosaurus hunted in packs or alone.')

        start()

    elif answer == '4':
        print('\n The Museums cast of a Diplodocus skeleton is on a tour around the UK.')
        print(' What did this giant look like and how did it hold its enormous neck?')

        start()

    elif answer == '5':
        print('\n This small meat-eater was one of the earliest dinosaurs.')
        print(' It was fast and agile and would have fed on animals like small reptiles and insects.')

        start()

    else:
        print('\n INVALID SELECTION!')

        start()


start()
