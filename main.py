from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class MainScreen(Screen):
    pass

class RuhaniScreen(Screen):
    def update_section_content(self, content):
        self.ids.section_label.text = content
    def back_to_home(self):
        screen_manager = self.manager
        screen_manager.current = 'main'     
       



class MDScreenManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.title = 'Graceful Gain'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        screen_manager = MDScreenManager()

        # Add screens to the screen manager
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(RuhaniScreen(name='ruhani'))

        return screen_manager

    
    def show_tailored_for_you(self):
       
        tailored_content = """
Unique Fitness Journey

Imagine a workout plan as unique as your fingerprints, finely tuned to your individuality.

Your Body, Your Goals:
Acknowledge your body's uniqueness. Your fitness goals shape a plan that's entirely your own.

Limitations as Opportunities:
Turn limitations into opportunities. Adapt the plan for safe and effective progress, even with past injuries or preferences.

Progress on Your Terms:
Gradual progress, confidence, and challenge in every step.

A Enjoyable Journey:
No more chore-like workouts. Embrace activities you enjoy, fostering consistency and positivity.

Results for You:
Personalized focus on what matters. Purposeful and rewarding workouts tailored to your objectives.
"""

        self.root.get_screen('ruhani').update_section_content(tailored_content)
        self.root.current = 'ruhani' 
        
    def show_evolving_with_you(self):
        evolving_content = """
Evolving with You: Personalized Fitness Journey

Your fitness journey is like a quest for personal transformation. Just as seasons change, your body evolves. "Evolving with you" is the acknowledgment that your journey is dynamic, adapting to your unique needs and desires.

Flexibility and Adaptability:
It's not one-size-fits-all. This deeply personalized experience weaves into your life, considering work, family, and personal commitments. Adjusting your routine, staying active, and being agile are the keys.

Mind and Emotions Matter:
It's not just physical; mental and emotional growth are vital. Self-awareness, self-compassion, and a positive mindset guide your journey.

In a changing world, "evolving with you" is about adaptability, growth, and empowerment. It's a lifelong voyage, reflecting your evolving self. Lace up your sneakers, set your intentions, and let "evolving with you" guide you to new horizons, one step at a time.
"""
        self.root.get_screen('ruhani').update_section_content(evolving_content)

        self.root.current = 'ruhani' 

    def show_smart_exercise_choices(self):
        smart_exercise_content = """
**Smart Exercise Choices: A Guide to Effective Workouts**

In the realm of fitness, making smart exercise choices is paramount to achieving your health and wellness goals. Gone are the days of mindlessly going through the motions – today, it's all about adopting a strategic approach that maximizes results while minimizing the risk of injury. From cardio enthusiasts to weightlifting aficionados, everyone can benefit from understanding the significance of intelligent exercise selection.
**1. Goal Alignment:**
Begin by defining your fitness goals. Are you aiming for muscle gain, weight loss, cardiovascular fitness, or overall functional strength? Each goal requires a different exercise approach. For instance, a muscle-building regimen would focus on resistance training, while weight loss might involve a mix of cardio and high-intensity interval training (HIIT).

**2. Target Muscle Groups:**
Identify the muscle groups you want to target. A well-rounded workout routine should include exercises that engage various muscle groups, ensuring balanced development and reducing the risk of muscle imbalances.

**3. Exercise Variation:**
Variety is the spice of life, and it holds true in fitness. Incorporate a mix of compound and isolation exercises to target different muscle fibers and movement patterns. Compound exercises, such as squats and deadlifts, engage multiple muscle groups simultaneously, while isolation exercises, like bicep curls, focus on specific muscles.
"""
        self.root.get_screen('ruhani').update_section_content(smart_exercise_content)

        self.root.current = 'ruhani' 

    def show_real_time_guidance(self):
        real_time_guidance_content = """
In today's tech-driven world, fitness has evolved with real-time guidance, making workouts interactive and dynamic. This isn't just about step counting; it's personalized interaction to enhance your fitness journey.

Interactive Workouts:
Real-time guidance offers personalized interaction during workouts, providing feedback, analyzing your form, and adjusting your routine for optimal results.

Form and Technique:
It assesses your form, reducing the risk of injury by offering cues to ensure correct execution of exercises.

Customized Workouts:
Your fitness level and goals shape your workouts. The system adapts intensity and exercises to keep you challenged but not overwhelmed.

Feedback Loop:
Receive insights as you go, tracking heart rate, calories burned, and reps completed, empowering data-driven decisions.

Motivation and Accountability:
Stay motivated with positive reinforcement, rewards for milestones, and reminders, like a virtual workout buddy.

Flexibility and Convenience:
Adapt your routine to life's unpredictability, customize workout duration, exercises, and intensity based on your schedule and energy levels.

"""
        self.root.get_screen('ruhani').update_section_content(real_time_guidance_content)
        self.root.current = 'ruhani' 

    def show_tracking_your_success(self):
        tracking_success_content = """

Tracking Progress for Fitness Transformation

Your fitness journey is a quest for personal transformation, and tracking progress is your trusty companion. It's about setting clear goals, quantifiable metrics, celebrating milestones, and staying motivated.

1. Clear Objectives:
Start with clear, achievable goals. Whether it's strength, endurance, or weight, defined objectives give direction to your journey.

2. Quantifiable Metrics:
Progress is measurable – weight, reps, distances, mood. These metrics offer tangible evidence of your journey and objective self-assessment.

3. Celebrating Milestones:
Every achievement matters, big or small. Celebrating milestones fuels your motivation and sense of accomplishment.

4. Identifying Patterns:
Tracking unveils trends. Discover what works best for you, adapt to your body's responses, and make informed adjustments.

5. Staying Accountable:
Accountability keeps you committed. Progress tracking is a personal responsibility, preventing lapses in workouts or nutrition.

6. Staying Motivated:
Visualize your journey, from photos to charts. Even in plateaus, it reignites your motivation to keep moving forward.
"""
        self.root.get_screen('ruhani').update_section_content(tracking_success_content)

        self.root.current = 'ruhani' 

    def show_recovery_and_prevention(self):
        recovery_prevention_content = """
Recovery and Prevention: Nurturing Your Body

In the fitness journey, it's not just about intense workouts; recovery and prevention are the unsung heroes.

1. The Science of Recovery:
It's the process where your body repairs, refuels, and balances after exertion. Neglecting it can lead to burnout and injuries.

2. Prioritizing Sleep:
7-9 hours of quality sleep are essential. It releases growth hormones, repairs cells, and restores energy levels.

3. Active Recovery:
Engage in low-intensity activities like gentle yoga or walks to stimulate healing without straining your body.

4. Proper Nutrition:
A balanced diet with protein, healthy fats, and nutrients supports repair and growth. Post-workout meals and hydration are crucial.

5. Hydration and Electrolytes:
Stay hydrated to transport nutrients and regulate temperature. Maintain electrolyte balance for muscle function.

6. Listen to Your Body:
Pay attention to fatigue, soreness, and pain. Overtraining can lead to injury; give your body time to heal.
"""

        self.root.get_screen('ruhani').update_section_content(recovery_prevention_content)

        self.root.current = 'ruhani' 

if __name__ == "__main__":
    MainApp().run()
