"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "../utils/supabaseClient";
import { API_BASE_URL } from "../utils/constants";

interface CreditCard {
  id: number;
  card_name: string;
  bank_provider: string;
  // Add other fields as necessary
}

export default function CreditCardList() {
  const [creditCards, setCreditCards] = useState<CreditCard[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    fetchCreditCards();
  }, []);

  const fetchCreditCards = async () => {
    setLoading(true);
    try {
      // Get the access token from Supabase auth
      const {
        data: { session },
      } = await supabase.auth.getSession();
      if (!session) {
        throw new Error("User not logged in");
      }
      const accessToken = session.access_token;
      console.log(accessToken);
      const response = await fetch(`${API_BASE_URL}/credit_cards/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        const errorData = await response.json(); // Parse error response
        // Check if the error is an array and extract the first error message
        const errorMessage = Array.isArray(errorData.detail)
          ? errorData.detail[0].msg
          : errorData.detail;
        throw new Error(errorMessage || "Failed to fetch credit cards");
      }
      const data = await response.json();
      setCreditCards(data);
      setError(null);
    } catch (error) {
      console.error("Error fetching credit cards:", error);
      setError("Failed to fetch credit cards. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  const handleAddCard = () => {
    router.push("/credit-cards/new");
  };

  const handleDeleteCard = async (cardId: number) => {
    setLoading(true);
    try {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      if (!session) {
        throw new Error("User not logged in");
      }
      const accessToken = session.access_token;
      const response = await fetch(`${API_BASE_URL}/credit_cards/${cardId}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        const errorMessage = Array.isArray(errorData.detail)
          ? errorData.detail[0].msg
          : errorData.detail;
        throw new Error(errorMessage || "Failed to delete credit card");
      }

      // Remove the deleted card from the state
      setCreditCards((prevCards) =>
        prevCards.filter((card) => card.id !== cardId)
      );
      setError(null);
    } catch (error) {
      console.error("Error deleting credit card:", error);
      setError("Failed to delete credit card. Please try again later.");
    } finally {
      setLoading(false);
    }
  };
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Credit Cards</h1>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <ul className="space-y-4">
          {creditCards.map((card) => (
            <li key={card.id} className="bg-white shadow-md rounded-md p-4">
              <div className="text-lg font-medium">{card.card_name}</div>
              <div className="text-gray-600">{card.bank_provider}</div>
              {/* ... (display other card details and buttons to edit/delete) */}
              <div className="mt-2">
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Edit
                </button>
                <button
                  className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2"
                  onClick={handleDeleteCard}
                >
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
      <button
        className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mt-4"
        onClick={handleAddCard}
      >
        Add New Card
      </button>
    </div>
  );
}
