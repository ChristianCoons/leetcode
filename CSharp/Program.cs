internal class Program
{
    private static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please specify which problem to test: dotnet run ProblemName");
            return;
        }

        Type? solutionType = Type.GetType($"Solutions.{args[0]}.Solution");
        if (solutionType == null)
        {
            Console.WriteLine($"Couldn't find solution for {args[0]}");
            return;
        }

        object? solution = Activator.CreateInstance(solutionType);
        var runTests = solutionType.GetMethod("RunTests");
        if (runTests is null)
        {
            Console.WriteLine($"No RunTests method found in {args[0]} solution");
            return;
        }
        runTests.Invoke(solution, null);
    }
}