from GameShop.task1.models import Buyer, Game


buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=17)  # Младше 18
buyer2 = Buyer.objects.create(name='Bob', balance=150.00, age=25)    # Старше 18
buyer3 = Buyer.objects.create(name='Charlie', balance=200.00, age=30)  # Старше 18

# Создание игр
game1 = Game.objects.create(title='Game One', cost=20.00, size=5.0,
                             description='An exciting adventure game.',
                             age_limited=True)  # Ограничение 18+
game2 = Game.objects.create(title='Game Two', cost=30.00, size=10.0,
                             description='A thrilling racing game.',
                             age_limited=False)  # Без ограничения
game3 = Game.objects.create(title='Game Three', cost=25.00, size=8.0,
                             description='A fun puzzle game.',
                             age_limited=True)

game1.buyers.set([buyer2])
game2.buyers.set([buyer2])
game3.buyers.set([buyer2])


game2.buyers.add(buyer1)