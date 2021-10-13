import menu


def start():
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

    elif answer == '6':
        print('\n As portrayed in the Jurassic Park movies,Velociraptor was recreated at twice its actual size and '
              ' closely modelled on Deinonychus.')
        print(' Though this was seen as unscientific at the time, soon after the first film was released, a dinosaur '
              ' of the same type,')
        print(' Utahraptor, was discovered, even larger than the virtual Velociraptors.')

        start()

    elif answer == '7':
        print('\n Ceratosaurus means horned lizard.')
        print(' The dinosaur was given this name because it had a row of sharp horns on its head and a row of small, '
              ' bony pieces of armour running along its back.')
        print(' It is not known what this body armour was for, but it could have been for protection from attack by '
              ' other Ceratosaurus or larger theropods such as Allosaurus and Torvosaurus.')

        start()

    elif answer == '8':
        print('\n Brachiosaurus held its head very high.')
        print(' It is likely to have eaten the leaves on tall tree-like plants.')

        start()

    elif answer == '9':
        print('\n A feathered dinosaur. One species, Microraptor gui had long flight feathers on all 4 limbs.')
        print(' It may have been capable of guided flight.')

        start()

    elif answer == '10':
        print('\n Albertosaurus was a close relative of Tyrannosaurus,')
        print(' but smaller and not as heavily built.')

        start()

    elif answer == '11':
        print('\n Utahraptor is similar to Velociraptor, but much larger.')

        start()

    elif answer == '12':
        print('\n The teeth of Allosaurus were 5-10cm long and curved backwards to prevent prey from escaping.')

        start()

    elif answer == '13':
        print('\n One of the largest armoured dinosaurus, Ankylosaurus had a wide,')
        print(' heavily armoured skull and a large tail club.')
        print(' It had a large gut space for digesting plant material.')

        start()

    elif answer == '14':
        print('\n Considered to be distinct from Brachiosaurus by some scientists,')
        print(' Giraffatitan is known from the fossils of several individuals.')

        start()

    elif answer == '15':
        print('\n Megalosaurus was one of the first dinosaurs discovered.')

        start()

    else:
        print('\n INVALID SELECTION!')

        start()


start()
