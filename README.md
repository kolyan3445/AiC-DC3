# AiC-DC3
ИСТбд-11, Лашманов Николай
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
Вариант 14.	Формируется матрица F следующим образом: если в В количество чисел, меньших К в нечетных столбцах в области 3 больше, чем сумма чисел в четных строках в области 2, то поменять в Е симметрично области 3 и 2 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
