unis = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(args):
        enrollment_list = []
        tuition_fees_list = []
        
        args = list(args)

        for i in args:
            a, b, c = i
            enrollment_list.append(b)
            tuition_fees_list.append(c)
        
        return enrollment_list, tuition_fees_list

def mean(args):
    return sum(args)/len(args)

def median(args):
    args.sort()
    lenght = len(args)
    if (lenght % 2 == 0):
        middle_index1 = lenght//2-1
        middle_index2 = (lenght//2)
        
        median_value = (args[middle_index1] + args[middle_index2])/2
    else:
        print(lenght//2, args[lenght//2])
        median_value = args[(lenght//2)]
    
    return median_value


enrollment_and_tuition_lists = enrollment_stats(unis)

enrollments = enrollment_and_tuition_lists[0]
tuition = enrollment_and_tuition_lists[1]

student_mean = mean(enrollments)
student_median = median(enrollments)


tuition_mean = mean(tuition)
tuition_median = median(tuition)

total_students = sum(enrollments)
total_tuition = sum(tuition)

print(f"****************\nTotal Students: {total_students:,}\nTotal Tuition: $ {total_tuition:,}\n\nStudent mean: {student_mean:,.2f}\nStudent median: {student_median:,}\n\nTuition mean: $ {tuition_mean:,.2f}\nTuition median: $ {tuition_median:,}\n****************")

