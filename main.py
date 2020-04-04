import math
while True:
  print('--------------------')
  print('---- Timer tool ----')
  print('--------------------')
  clock_input = float(input('--> Clock input [Hz] = '))
  goal_freq = float(input('--> Goal frequency [Hz] = '))
  max_prescaler = 2**int(input('--> Prescaler [bits] = ')) - 1
  max_compare = 2**int(input ('--> Compare registrer [bits] = ')) - 1 
  min_error = float(input('--> Max error [%] = '))
  print('\n')
  min_prescaler = math.ceil(clock_input/(goal_freq*max_compare))

  if math.ceil(clock_input/goal_freq) < max_prescaler:
    max_prescaler = math.ceil(clock_input/goal_freq)

  min_err = 5;
  solution = False
  for prescaler in range(min_prescaler, max_prescaler):

    compare = math.ceil( clock_input/(goal_freq*prescaler) )
    resulting_freq = clock_input/(prescaler*compare)
    rel_err = 100.0*math.fabs(goal_freq-resulting_freq)/goal_freq
    if rel_err <= min_err:
      solution = True
      min_err = rel_err
      print('Prescaler = ' + str(prescaler) + ', Compare = ' + str(compare) + ', OutFreq = ' + str(resulting_freq) + ', relErr = ' + str(rel_err) )

  if solution == False:
    print('ERROR: No solution was found')

  print('\n\n')