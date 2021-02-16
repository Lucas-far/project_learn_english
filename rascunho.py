

from gramatica.preposicao import *

# prep = [
#     about_[0], above_[0], across_[0], after_[0], against_[0], ago_[0], among_[0], around_[0], as_[0], at_[0],
#     before_[0], behind_[0], below_[0], between_[0], by_[0], down_[0], during_[0], for_[0], from_[0], in_[0],
#     in_front_of_[0], into_[0], like_[0], next_to_[0], of_[0], on_[0], out_[0], over_[0], since_[0], through_[0],
#     to_[0], towards_[0], under_[0], underneath_[0], until_[0], up_[0], with_[0], without_[0]
# ]



# prep_pt_br = [
#     about_[1], above_[1], across_[1], after_[1], against_[1], ago_[1], among_[1], around_[1], as_[1], at_[1],
#     before_[1], behind_[1], below_[1], between_[1], by_[1], down_[1], during_[1], for_[1], from_[1], in_[1],
#     in_front_of_[1], into_[1], like_[1], next_to_[1], of_[1], on_[1], out_[1], over_[1], since_[1], through_[1],
#     to_[1], towards_[1], under_[1], underneath_[1], until_[1], up_[1], with_[1], without_[1]
# ]



print(prep, '\n', len(prep))
print(prep_pt_br, '\n', len(prep_pt_br))

print('\n')
print(f'{len(prep) = }')
print(f'{len(prep_pt_br) = }')
print('\n')
for word in zip(prep, prep_pt_br):
    print(word)