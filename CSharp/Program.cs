internal class Program
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please specify which problem to test: dotnet run ProblemName");
            return;
        }

        // Get the solution type dynamically based on the provided problem name
        Type? solutionType = Type.GetType($"Solutions.{args[0]}.Solution");
        if (solutionType == null)
        {
            Console.WriteLine($"Couldn't find solution for {args[0]}");
            return;
        }

        // Create an instance of the solution class
        object? solution = Activator.CreateInstance(solutionType);
        if (solution == null)
        {
            Console.WriteLine($"Failed to create an instance of {args[0]} solution");
            return;
        }

        // Get the RunTests method from the solution class
        var runTests = solutionType.GetMethod("RunTests");
        if (runTests == null)
        {
            Console.WriteLine($"No RunTests method found in {args[0]} solution");
            return;
        }

        // Invoke the RunTests method
        try
        {
            runTests.Invoke(solution, null);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred while running tests: {ex.Message}");
        }
    }
}