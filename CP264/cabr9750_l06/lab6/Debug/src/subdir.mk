################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/driver_main.c \
../src/llist.c \
../src/llqueue.c \
../src/llstack.c 

OBJS += \
./src/driver_main.o \
./src/llist.o \
./src/llqueue.o \
./src/llstack.o 

C_DEPS += \
./src/driver_main.d \
./src/llist.d \
./src/llqueue.d \
./src/llstack.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


